import re,json
B=[('accelerators','accelerators.md'),('foundry','foundry-semicap.md'),('hbm','hbm-packaging.md'),('dcbuild','dc-build.md'),('dcelec','dc-electrical-cooling.md'),('power','power.md')]
pat=re.compile(r'^(\s*)- \*\*(.+?)\*\*(?: \[([A-Z ]+)\])? \(depth (\d+)[^)]*\)\s*[—:-]?\s*(.*)$')
CANON=[(r'^HBM stacks','hbm-stacks'),(r'CoWoS-S / -L / -R|2\.5D packaging: TSMC CoWoS','cowos'),(r'^IC substrate \(ABF','abf-substrate'),(r'^ABF build-up film','abf-film'),(r'^T-glass','t-glass'),(r'Silicon interposer','si-interposer'),(r'^OSAT CoWoS','osat-cowos'),(r'^TC bonders','tc-bonders'),
 (r'^Compute die: leading-edge|^Leading-edge logic die','logic-die'),(r'^Gallium \(raw\)|Bauxite / alumina refining → gallium','gallium'),(r'^Fluorspar','fluorspar'),(r'^Grid interconnect / large-load pause|^Grid interconnection queue','grid-queue'),
 (r'^Indium','indium'),(r'^Germanium','germanium'),(r'^Copper \(busbar|^Oxygen-free copper rod','copper'),(r'^SF6','sf6'),(r'^Vacuum interrupters','vacuum-interrupters'),(r'^Helium','helium')]
def canon(n):
  for p,c in CANON:
    if re.search(p,n): return c
url=re.compile(r'https?://[^\s,)]+')
nodes={};order=[];slug=lambda s:re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')[:50]
root={'id':'root','name':'AI accelerator running in an energized data center','tag':'BINDING','depth':0,'parents':[],'children':[],'evidence':'Union of the six branch roots (SPEC.md).','source':[],'lead_time':None,'branch':'root','also_in':[]}
nodes['root']=root
for br,f in B:
  stack={}
  for line in open(f):
    m=pat.match(line.rstrip('\n'))
    if not m: continue
    ind,name,tag,d,rest=m.groups();d=int(d)+1;tag=tag or 'GROUP'
    lvl=len(ind)//2
    c=canon(name); nid=c or f'{br}:{slug(name)}'
    par=stack.get(lvl-1,'root')
    lt=None; mm=re.search(r'Lead/build time:\s*(.*?)(?:\.\s*Feeds:|$)',rest)
    if mm: lt=mm.group(1).strip()
    if nid in nodes and nid!='root':
      n=nodes[nid]; n['also_in'].append({'branch':br,'name':name,'tag':tag,'evidence':rest,'source':url.findall(rest)})
      if tag=='BINDING' and n['tag']!='BINDING': n['tag']='BINDING'
      n['source']=sorted(set(n['source']+url.findall(rest)))
      if not n['lead_time'] and lt: n['lead_time']=lt
      n['depth']=min(n['depth'],d)
    else:
      nodes[nid]={'id':nid,'name':name,'tag':tag,'depth':d,'parents':[],'children':[],'evidence':rest,'source':url.findall(rest),'lead_time':lt,'branch':br,'also_in':[],'file':f}
      order.append(nid)
    if par not in nodes[nid]['parents']: nodes[nid]['parents'].append(par)
    if nid not in nodes[par]['children']: nodes[par]['children'].append(nid)
    stack[lvl]=nid
json.dump({'generated':'2026-10-23','spec':'SPEC.md','note':'depth = branch depth+1 under unified root; min over occurrences. Numbers verbatim from branch files; none added.','nodes':list(nodes.values())},open('TREE.json','w'),indent=1,ensure_ascii=False)
# markdown tree
seen=set();out=[]
def walk(nid,lvl):
  n=nodes[nid]
  if nid in seen:
    out.append('  '*lvl+f'- ↪ **{n["name"]}** [{n["tag"]}] — see `#{nid}` (shared node)');return
  seen.add(nid)
  if nid=='root': out.append(f'- **{n["name"]}** [BINDING] (depth 0) <a id="root"></a>')
  else:
    x=''
    if len(n['parents'])>1 or n['also_in']: x=f' 🔗 shared: parents {", ".join("`"+p+"`" for p in n["parents"])}'+(f'; also described in {", ".join(a["branch"] for a in n["also_in"])}' if n['also_in'] else '')
    out.append('  '*lvl+f'- **{n["name"]}** [{n["tag"]}] (depth {n["depth"]}) <a id="{nid}"></a> `{nid}` ({n["file"]}){x} — {n["evidence"]}')
    for a in n['also_in']: out.append('  '*(lvl+1)+f'- _also ({a["branch"]}, as "{a["name"]}", [{a["tag"]}])_: {a["evidence"]}')
  for c in n['children']: walk(c,lvl+1)
walk('root',0)
open('/tmp/treebody.md','w').write('\n'.join(out))
from collections import Counter
print(len(nodes),Counter(n['tag'] for n in nodes.values()))
print([ (n['id'],n['parents']) for n in nodes.values() if len(n['parents'])>1])
print(sorted((n['depth'],n['id']) for n in nodes.values() if n['tag']=='POTENTIAL')[-12:])
print([n['name'] for n in nodes.values() if n['tag']=='GAP'])

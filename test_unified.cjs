const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
function subject(){
 const records=new Map();
 const context={console,Map,Set,Date,JSON,Promise,Cloud:{},RuntimeAssets:{},window:{addEventListener(){}},document:{},OfflineLibrary:{h:v=>String(v)},UI:{openSettings(){}},OfflineAccess:{},SaveBridge:{sync:async()=>{},refreshViews(){}},Learning:{cardInfo:()=>({title:'old'}),reviewOne(){},focus(){}},Store:{get:(k,d)=>records.has(k)?records.get(k):d,set:(k,v)=>records.set(k,v),getRaw:(k,d)=>records.has(k)?records.get(k):d,setRaw:(k,v)=>records.set(k,v)}};
 vm.createContext(context);vm.runInContext(fs.readFileSync(__dirname+'/web/unified.js','utf8')+'\nthis.subject=Unified;',context);return {u:context.subject,context,records};
}
test('one index merges numbered references, legacy sources and equivalent judged exercises',()=>{
 const {u}=subject();const p={id:'lc-two-sum',number:'1',title:'Two Sum',topics:['Array'],companies:{},kind:'reference'};
 const old={key:'lc-1',number:1,title:'Two Sum',tags:['Hash Map']};
 const rows=u.makeIndex({problems:[p]},[old,{key:'topic-graph',number:null,title:'Graph basics',tags:['Graph'],difficulty:'Unknown',solutionCount:1}], [{id:500,title:'Two Sum',tags:['Array']},{id:501,title:'Pattern printing',tags:['Loops']}]);
 assert.equal(rows.length,3);const two=rows.find(r=>r.id==='lc-two-sum');assert.equal(two.legacy.length,1);assert.equal(two.exercises[0].id,500);assert.ok(two.topics.includes('Hash Map'));assert.ok(rows.some(r=>r.id==='task-501'));
});
test('reference implementations deduplicate normalized language and whitespace',()=>{
 const {u}=subject();const rows=u.uniqueSolutions([{language:'py',code:'return 1\r\n'},{language:'python3',code:'return 1   \n'},{language:'cpp',code:'return 1;'}]);assert.equal(rows.length,2);
});
test('draft metadata updates retain solved status and old bookmarks',()=>{
 const {u,records}=subject();records.set('library_progress',{'lc-1':{star:true}});const p={id:'lc-two-sum',number:'1'};
 assert.equal(u.state(p).star,true);u.setState(p.id,{status:'solved'});u.setState(p.id,{language:'python'});assert.equal(u.state(p).status,'solved');assert.equal(u.state(p).star,true);
});
test('practice filtering includes attached judged exercises',()=>{
 const {u}=subject();u.scope='practice';u.items=[{id:'ref-a',title:'Example',topics:['Array'],companies:{},kind:'reference',difficulty:'Easy',exercises:[{id:1}]},{id:'ref-b',title:'Reading only',topics:[],companies:{},kind:'reference',difficulty:'Easy'}];assert.equal(u.filtered().length,1);
});
test('reference mistakes open the correct question from the shared revision system',()=>{
 const {u,context,records}=subject();records.set('revision_state',{'reference:lc-two-sum':{source:'reference'}});let route;u.open=(view,id)=>route={view,id};context.Learning.reviewOne('reference:lc-two-sum');assert.equal(route.view,'question');assert.equal(route.id,'lc-two-sum');
});
test('browser function worker checks solutions without Node or a cloud compiler in the app',()=>{
 let result;const self={postMessage:value=>{result=value;}};const context={self,performance,structuredClone,JSON,Error,Set};vm.createContext(context);vm.runInContext(fs.readFileSync(__dirname+'/web/function-worker.js','utf8'),context);
 self.onmessage({data:{function:'twoSum',code:'function twoSum(nums,target){const seen=new Map();for(let i=0;i<nums.length;i++){if(seen.has(target-nums[i]))return [seen.get(target-nums[i]),i];seen.set(nums[i],i)}}',mode:'submit',tests:[{args:[[2,7,11,15],9],expected:[0,1]},{args:[[3,2,4],6],expected:[1,2]}]}});
 assert.equal(result.accepted,true);assert.equal(result.cases.length,2);
 self.onmessage({data:{function:'solve',code:'function solve(){return {0:1,1:2}}',mode:'submit',tests:[{args:[],expected:[1,2]}]}});assert.equal(result.accepted,false);
 self.onmessage({data:{function:'solve',code:'function solve(){throw new Error("example")}',mode:'custom',tests:[{args:[]}]}});assert.equal(result.verdict,'Runtime error');
});

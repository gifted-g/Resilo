import { useState } from 'react'
export default function AIAssistant({deploymentId}){
  const [q,setQ] = useState('Why did deploy fail?')
  const [ans,setAns] = useState(null)
  const [loading,setLoading] = useState(false)
  async function ask(){
    setLoading(true)
    const res = await fetch('/api/ai/ask', {method:'POST', body: JSON.stringify({query:q, context:{deploymentId}}), headers:{'Content-Type':'application/json'}})
    const j = await res.json()
    setAns(j)
    setLoading(false)
  }
  return (
    <div>
      <h3 className="font-semibold">AI Ops Assistant</h3>
      <textarea value={q} onChange={e=>setQ(e.target.value)} className="w-full p-2 border rounded mt-2" rows={4} />
      <div className="mt-2"><button onClick={ask} className="px-3 py-1 bg-indigo-600 text-white rounded">{loading?'...':'Ask'}</button></div>
      {ans && <div className="mt-3 p-2 bg-gray-50 rounded"><strong>Answer:</strong><div>{ans.answer}</div><pre className="mt-2 text-xs">{JSON.stringify(ans.recommendation,null,2)}</pre></div>}
    </div>
  )
}

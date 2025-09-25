import dynamic from 'next/dynamic'
const AIAssistant = dynamic(()=>import('../components/AIAssistant'), { ssr:false })
export default function Deployments(){
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Deployments</h1>
      <div className="grid grid-cols-2 gap-4">
        <div className="p-4 border rounded">Deployment list (stub)</div>
        <div className="p-4 border rounded"><AIAssistant deploymentId="deploy-111" /></div>
      </div>
    </div>
  )
}

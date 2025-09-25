import Link from 'next/link'
export default function Home(){
  return (
    <div className="p-8 font-sans bg-white min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Resilo Dashboard (POC)</h1>
      <p className="mb-4">Go to <Link href='/deployments'><a className='text-indigo-600'>Deployments</a></Link></p>
    </div>
  )
}

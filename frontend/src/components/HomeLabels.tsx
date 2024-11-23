type HomeLabelsProps = {
  upperText: string;
  lowerText: string;
}

export function HomeLabels({ upperText, lowerText }: Readonly<HomeLabelsProps>) {
  return (
    <div className='bg-sky-100 w-full h-full flex flex-col px-8 gap-2 rounded-3xl py-4'>
      <h2 className='text-center text-3xl font-semibold'>{upperText}</h2>
      {/* Add a line that sepparates the two labels */}
      <hr className='border-sky-700 w-full border-[1.5px]' />
      <h3 className='text-center text-2xl ' >{lowerText}</h3>

    </div >
  )
}
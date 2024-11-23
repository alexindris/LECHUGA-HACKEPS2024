
type ErrorMessageProps = {
  errorMessage: string | null;
}

export function ErrorMessage({ errorMessage }: Readonly<ErrorMessageProps>) {
  if (!errorMessage) {
    return <></>;
  }
  return (
    <div className='bg-red-500 text-white p-4 rounded-lg'>
      <p>{errorMessage}</p>
    </div>
  );

}
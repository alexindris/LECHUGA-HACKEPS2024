import { HomeLabels } from '@/components/HomeLabels';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { createFileRoute, Link } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  component: HomeComponent,
});

export function HomeComponent() {
  return (
    <div className="flex flex-col h-screen w-full bg-sky-100">
      <header className="bg-sky-200 w-full h-16 flex items-center justify-center">
        <img src="/home_logo.png" alt="Home Logo" className="h-10 sm:h-12" />
      </header>


      <div
        className="flex flex-col md:flex-row w-full h-full items-center justify-center px-8 md:px-16 lg:px-32 py-4 "
        style={{
          backgroundImage: `url("/home_bg.png")`,
          backgroundSize: "90% auto",
          backgroundPosition: "center",
          backgroundRepeat: "no-repeat",
        }}
      >
        <div className='flex items-center justify-center flex-col gap-16 w-full'>
          <Card className="bg-white rounded-[3.6rem] w-full max-w-md md:max-w-lg py-8 px-4 ">
            <CardHeader className=" sm:p-8 md:p-12 flex flex-col text-center">
              <CardTitle className="text-3xl sm:text-4xl md:text-5xl text-sky-800 font-bold">
                HOW TO USE
              </CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col gap-8">
              <HomeLabels upperText="FIRST STEP" lowerText="Sign up" />
              <HomeLabels upperText="SECOND STEP" lowerText="Enter a new parking" />
              <HomeLabels upperText="THIRD STEP" lowerText="Control parking access!" />
            </CardContent>
          </Card>
          <div className='flex flex-row gap-4 items-center justify-center h-full w-full'>
            <Button className='bg-sky-700 rounded-3xl text-3xl p-10' >
              <Link to='/auth/signup'>Sign up</Link>
            </Button>
            <span className='text-sky-700 text-3xl font-bold'>OR</span>
            <Button className='bg-sky-700 rounded-3xl text-3xl p-10' >
              <Link to='/auth/signin'>Sign in</Link>
            </Button>
          </div>
        </div>
      </div>


    </div>
  );
}
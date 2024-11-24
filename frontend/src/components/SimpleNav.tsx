import {
  Tabs,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"
import { useNavigate, useRouterState } from '@tanstack/react-router'
import { Avatar, AvatarFallback, AvatarImage } from './ui/avatar';


type TabsProps = {
  disabledParkingTab: boolean;
  activeTab?: string;
}

export default function SimpleNav({ disabledParkingTab, activeTab = 'home' }: Readonly<TabsProps>) {

  // const navItems = [
  //   { name: "Home", href: "#" },
  //   { name: "Parking", href: "#" },
  // ]

  const navigate = useNavigate();
  const router = useRouterState();

  return (
    <header className="flex flex-col bg-sky-200 w-full h-16 p-1 ">
      <div className='flex items-center justify-between w-full  px-3'>
        <img src="/home_logo.png" alt="Home Logo" className="h-10  pt-1 " />
        <Tabs defaultValue={activeTab} className="w-[300px] flex border rounded-xl border-white">
          <TabsList className="grid w-full grid-cols-2 h-full p-0  ">
            <TabsTrigger
              onClick={() => { router.location.pathname !== '/home' && navigate({ to: '/home' }) }}
              value="home"
              className="data-[state=active]:bg-white data-[state=active]:text-black text-gray-600 px-4 py-2 rounded-xl transition-colors">
              Home
            </TabsTrigger>
            <TabsTrigger
              disabled={disabledParkingTab}
              value="parking"
              className="data-[state=active]:bg-white data-[state=active]:text-black text-gray-600 px-4 py-2 rounded-xl transition-colors">
              Parking
            </TabsTrigger>
          </TabsList>
        </Tabs>
        <Avatar className=' rounded-full'>
          <AvatarImage src="https://github.com/shadcn.png" />
          <AvatarFallback>XD</AvatarFallback>
        </Avatar>
      </div>
    </header>
  )
}


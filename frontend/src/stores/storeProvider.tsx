import React, { createContext, useContext, useMemo } from "react";
import { ParkingStore, UserStore } from './store';

const UserStoreContext = createContext<UserStore | null>(null);
const ParkingStoreContext = createContext<ParkingStore | null>(null);

export const AppStoreProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const userStore = useMemo(() => new UserStore(), []);
  const parkingStore = useMemo(() => new ParkingStore(), [])

  return (
    <UserStoreContext.Provider value={userStore}>
      <ParkingStoreContext.Provider value={parkingStore}>
        {children}
      </ParkingStoreContext.Provider>
    </UserStoreContext.Provider>
  );
};

export const useUserStore = () => {
  const context = useContext(UserStoreContext);
  if (!context) {
    throw new Error(
      "useUserStore must be used within a AppStoreProvider"
    );
  }
  return context;
};
export const useParkingStore = () => {
  const context = useContext(ParkingStoreContext);
  if (!context) {
    throw new Error(
      "useParkingStore must be used within a AppStoreProvider"
    );
  }
  return context;
};

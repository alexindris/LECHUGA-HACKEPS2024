import React, { createContext, useContext } from "react";
import { CounterStore } from "@/stores/store";

const CounterStoreContext = createContext<CounterStore | null>(null);

export const CounterStoreProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const store = new CounterStore();

  return (
    <CounterStoreContext.Provider value={store}>
      {children}
    </CounterStoreContext.Provider>
  );
};

export const useCounterStore = () => {
  const context = useContext(CounterStoreContext);
  if (!context) {
    throw new Error(
      "useCounterStore must be used within a CounterStoreProvider"
    );
  }
  return context;
};

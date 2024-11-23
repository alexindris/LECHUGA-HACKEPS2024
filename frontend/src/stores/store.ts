import { action, makeAutoObservable, observable } from "mobx";

export class CounterStore {
  @observable count = 0;

  constructor() {
    makeAutoObservable(this);
  }

  @action increment() {
    this.count++;
  }

  @action decrement() {
    this.count--;
  }
}

// export const counterStore = new CounterStore();

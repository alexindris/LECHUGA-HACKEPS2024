import { LOGIN_USER } from '@/lib/api';
import { apolloClient } from '@/lib/utils';
import { action, flow, makeAutoObservable, observable } from "mobx";

export class UserStore {
  @observable userToken: string | null = null;
  client = apolloClient

  constructor() {
    makeAutoObservable(this);
  }

  @action setToken(token: string) {
    this.userToken = token;
  }

  @action clearToken() {
    this.userToken = null;
  }

  @flow async login(email: string, password: string) {
    try {
      const { data } = await this.client.mutate({
        mutation: LOGIN_USER,
        variables: { email, password },
      });
      this.setToken(data?.loginUser?.token ?? '');
    } catch (e: any) {
      return { errorMessage: e.message }
    }
  }
}

class Parking {
  id: number;
  status: boolean;

  constructor(id: number, status: boolean) {
    this.id = id;
    this.status = status;
  }

  toggleStatus(): void {
    this.status = !this.status;
  }

  displayDetails(): string {
    return `Parking ID: ${this.id}, Status: ${this.status ? 'Occupied' : 'Available'}`;
  }
}

export class ParkingStore {
  @observable parkings: Parking[] = [];

  constructor() {
    makeAutoObservable(this);
  }

  @action addParking(parking: Parking) {
    this.parkings.push(parking);
  }

}

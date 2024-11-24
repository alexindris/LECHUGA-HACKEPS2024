import { ParkingType } from '@/__generated__/graphql';
import { CREATE_PARKING, GET_ALL_PARKINGS, LOGIN_USER } from '@/lib/api';
import { apolloClient } from '@/lib/utils';
import { action, flow, makeAutoObservable, observable } from "mobx";

export class UserStore {
  @observable userToken: string | null = null;

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
      const { data } = await apolloClient.mutate({
        mutation: LOGIN_USER,
        variables: { email, password },
      });
      this.setToken(data?.loginUser?.token ?? '');
      return { token: this.userToken }
    } catch (e: any) {
      return { errorMessage: e.message }
    }
  }
}

export class ParkingStore {
  @observable parkings: ParkingType[] = [];

  constructor() {
    makeAutoObservable(this);
  }

  @action async createParking(name: string, address: string, totalLots: number) {
    try {
      const a = await apolloClient.mutate({
        mutation: CREATE_PARKING,
        variables: { name: name, address: address, totalLots: totalLots },
      });

      if (a.data?.createParking)
        this.parkings.push(a.data?.createParking.parking)

    } catch (e) {
      return { error: "Check the address" }
    }

  }

  @flow async getAllParkings() {
    try {
      const { data } = await apolloClient.query({
        query: GET_ALL_PARKINGS,
      });
      console.log(data)

      this.parkings = data?.allParkings.filter((parking) => parking !== null) ?? [];

    } catch (e: any) {
      return { errorMessage: e.message }
    }
  }

}

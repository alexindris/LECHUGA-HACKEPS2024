/* eslint-disable */
import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type MakeEmpty<T extends { [key: string]: unknown }, K extends keyof T> = { [_ in K]?: never };
export type Incremental<T> = T | { [P in keyof T]?: P extends ' $fragmentName' | '__typename' ? T[P] : never };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: { input: string; output: string; }
  String: { input: string; output: string; }
  Boolean: { input: boolean; output: boolean; }
  Int: { input: number; output: number; }
  Float: { input: number; output: number; }
  /**
   * The `DateTime` scalar type represents a DateTime
   * value as specified by
   * [iso8601](https://en.wikipedia.org/wiki/ISO_8601).
   */
  DateTime: { input: any; output: any; }
  ParkingID: { input: any; output: any; }
  UserID: { input: any; output: any; }
};

export type CreateParkingMutation = {
  __typename?: 'CreateParkingMutation';
  parking: ParkingType;
};

export type CreateUserMutation = {
  __typename?: 'CreateUserMutation';
  user: UserType;
};

export type HealthType = {
  __typename?: 'HealthType';
  status: Scalars['String']['output'];
  time: Scalars['DateTime']['output'];
};

export type LoginUserMutation = {
  __typename?: 'LoginUserMutation';
  token: Scalars['String']['output'];
};

export type Mutation = {
  __typename?: 'Mutation';
  createParking: CreateParkingMutation;
  createUser: CreateUserMutation;
  loginUser: LoginUserMutation;
};


export type MutationCreateParkingArgs = {
  address: Scalars['String']['input'];
  name: Scalars['String']['input'];
  totalLots: Scalars['Int']['input'];
};


export type MutationCreateUserArgs = {
  email: Scalars['String']['input'];
  name: Scalars['String']['input'];
  password: Scalars['String']['input'];
};


export type MutationLoginUserArgs = {
  email: Scalars['String']['input'];
  password: Scalars['String']['input'];
};

export type ParkingEntry = {
  __typename?: 'ParkingEntry';
  createdAt: Scalars['DateTime']['output'];
  entryType: ParkingStatusEnum;
};

export enum ParkingStatusEnum {
  Entrance = 'ENTRANCE',
  Exit = 'EXIT'
}

export type ParkingType = {
  __typename?: 'ParkingType';
  address: Scalars['String']['output'];
  entries: Array<Maybe<ParkingEntry>>;
  identifier: Scalars['ParkingID']['output'];
  name: Scalars['String']['output'];
  occupiedLots: Scalars['Int']['output'];
  totalLots: Scalars['Int']['output'];
};

export type Query = {
  __typename?: 'Query';
  allParkings: Array<Maybe<ParkingType>>;
  health: HealthType;
  me: UserType;
  parking?: Maybe<ParkingType>;
};


export type QueryParkingArgs = {
  identifier: Scalars['String']['input'];
};

export type UserType = {
  __typename?: 'UserType';
  email: Scalars['String']['output'];
  identifier: Scalars['UserID']['output'];
  name: Scalars['String']['output'];
};

export type HealthQueryVariables = Exact<{ [key: string]: never; }>;


export type HealthQuery = { __typename?: 'Query', health: { __typename?: 'HealthType', status: string, time: any } };

export type LoginUsrMutationVariables = Exact<{
  email: Scalars['String']['input'];
  password: Scalars['String']['input'];
}>;


export type LoginUsrMutation = { __typename?: 'Mutation', loginUser: { __typename?: 'LoginUserMutation', token: string } };

export type CreateUsrMutationVariables = Exact<{
  email: Scalars['String']['input'];
  name: Scalars['String']['input'];
  password: Scalars['String']['input'];
}>;


export type CreateUsrMutation = { __typename?: 'Mutation', createUser: { __typename?: 'CreateUserMutation', user: { __typename?: 'UserType', identifier: any, name: string, email: string } } };

export type ParkingQueryVariables = Exact<{ [key: string]: never; }>;


export type ParkingQuery = { __typename?: 'Query', allParkings: Array<{ __typename?: 'ParkingType', identifier: any, name: string, address: string, totalLots: number, occupiedLots: number, entries: Array<{ __typename?: 'ParkingEntry', entryType: ParkingStatusEnum, createdAt: any } | null> } | null> };

export type GetParkingQueryVariables = Exact<{
  identifier: Scalars['String']['input'];
}>;


export type GetParkingQuery = { __typename?: 'Query', parking?: { __typename?: 'ParkingType', identifier: any, name: string, address: string, totalLots: number, occupiedLots: number, entries: Array<{ __typename?: 'ParkingEntry', entryType: ParkingStatusEnum, createdAt: any } | null> } | null };

export type CreateParkinggMutationVariables = Exact<{
  name: Scalars['String']['input'];
  address: Scalars['String']['input'];
  totalLots: Scalars['Int']['input'];
}>;


export type CreateParkinggMutation = { __typename?: 'Mutation', createParking: { __typename?: 'CreateParkingMutation', parking: { __typename?: 'ParkingType', identifier: any, name: string, address: string, totalLots: number, occupiedLots: number, entries: Array<{ __typename?: 'ParkingEntry', entryType: ParkingStatusEnum, createdAt: any } | null> } } };


export const HealthDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"Health"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"health"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"status"}},{"kind":"Field","name":{"kind":"Name","value":"time"}}]}}]}}]} as unknown as DocumentNode<HealthQuery, HealthQueryVariables>;
export const LoginUsrDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"LoginUsr"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"email"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"password"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"loginUser"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"email"},"value":{"kind":"Variable","name":{"kind":"Name","value":"email"}}},{"kind":"Argument","name":{"kind":"Name","value":"password"},"value":{"kind":"Variable","name":{"kind":"Name","value":"password"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"token"}}]}}]}}]} as unknown as DocumentNode<LoginUsrMutation, LoginUsrMutationVariables>;
export const CreateUsrDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"CreateUsr"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"email"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"name"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"password"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"createUser"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"email"},"value":{"kind":"Variable","name":{"kind":"Name","value":"email"}}},{"kind":"Argument","name":{"kind":"Name","value":"name"},"value":{"kind":"Variable","name":{"kind":"Name","value":"name"}}},{"kind":"Argument","name":{"kind":"Name","value":"password"},"value":{"kind":"Variable","name":{"kind":"Name","value":"password"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"user"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"identifier"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"email"}}]}}]}}]}}]} as unknown as DocumentNode<CreateUsrMutation, CreateUsrMutationVariables>;
export const ParkingDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"Parking"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"allParkings"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"identifier"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"address"}},{"kind":"Field","name":{"kind":"Name","value":"totalLots"}},{"kind":"Field","name":{"kind":"Name","value":"occupiedLots"}},{"kind":"Field","name":{"kind":"Name","value":"entries"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"entryType"}},{"kind":"Field","name":{"kind":"Name","value":"createdAt"}}]}}]}}]}}]} as unknown as DocumentNode<ParkingQuery, ParkingQueryVariables>;
export const GetParkingDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"GetParking"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"identifier"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"parking"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"identifier"},"value":{"kind":"Variable","name":{"kind":"Name","value":"identifier"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"identifier"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"address"}},{"kind":"Field","name":{"kind":"Name","value":"totalLots"}},{"kind":"Field","name":{"kind":"Name","value":"occupiedLots"}},{"kind":"Field","name":{"kind":"Name","value":"entries"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"entryType"}},{"kind":"Field","name":{"kind":"Name","value":"createdAt"}}]}}]}}]}}]} as unknown as DocumentNode<GetParkingQuery, GetParkingQueryVariables>;
export const CreateParkinggDocument = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"mutation","name":{"kind":"Name","value":"CreateParkingg"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"name"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"address"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"totalLots"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"Int"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"createParking"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"address"},"value":{"kind":"Variable","name":{"kind":"Name","value":"address"}}},{"kind":"Argument","name":{"kind":"Name","value":"name"},"value":{"kind":"Variable","name":{"kind":"Name","value":"name"}}},{"kind":"Argument","name":{"kind":"Name","value":"totalLots"},"value":{"kind":"Variable","name":{"kind":"Name","value":"totalLots"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"parking"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"identifier"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"address"}},{"kind":"Field","name":{"kind":"Name","value":"totalLots"}},{"kind":"Field","name":{"kind":"Name","value":"occupiedLots"}},{"kind":"Field","name":{"kind":"Name","value":"entries"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"entryType"}},{"kind":"Field","name":{"kind":"Name","value":"createdAt"}}]}}]}}]}}]}}]} as unknown as DocumentNode<CreateParkinggMutation, CreateParkinggMutationVariables>;
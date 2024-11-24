/* eslint-disable */
import * as types from './graphql';
import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';

/**
 * Map of all GraphQL operations in the project.
 *
 * This map has several performance disadvantages:
 * 1. It is not tree-shakeable, so it will include all operations in the project.
 * 2. It is not minifiable, so the string of a GraphQL query will be multiple times inside the bundle.
 * 3. It does not support dead code elimination, so it will add unused operations.
 *
 * Therefore it is highly recommended to use the babel or swc plugin for production.
 * Learn more about it here: https://the-guild.dev/graphql/codegen/plugins/presets/preset-client#reducing-bundle-size
 */
const documents = {
    "\n  query Health {\n    health {\n      status\n      time\n    }\n  }\n": types.HealthDocument,
    "\n  mutation LoginUsr($email: String!, $password: String!){\n    loginUser(email:$email, password: $password) {\n        token,\n    }\n  }\n": types.LoginUsrDocument,
    "\n  mutation CreateUsr( $email: String!, $name: String!, $password: String!){\n    createUser(email:$email, name:$name, password: $password) {\n        user {\n          identifier,\n          name,\n          email,\n        }\n    }\n  }\n": types.CreateUsrDocument,
    "\n  query Parking {\n    allParkings {\n        identifier\n        name\n        address\n        totalLots\n        occupiedLots\n        entries {\n            entryType\n            createdAt\n        }\n    }\n}\n": types.ParkingDocument,
    "\n  query GetParking($identifier: String!) {\n    parking(identifier: $identifier) {\n        identifier\n        name\n        address\n        totalLots\n        occupiedLots\n        entries {\n          entryType\n          createdAt\n        }\n    }\n}\n": types.GetParkingDocument,
};

/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 *
 *
 * @example
 * ```ts
 * const query = gql(`query GetUser($id: ID!) { user(id: $id) { name } }`);
 * ```
 *
 * The query argument is unknown!
 * Please regenerate the types.
 */
export function gql(source: string): unknown;

/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function gql(source: "\n  query Health {\n    health {\n      status\n      time\n    }\n  }\n"): (typeof documents)["\n  query Health {\n    health {\n      status\n      time\n    }\n  }\n"];
/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function gql(source: "\n  mutation LoginUsr($email: String!, $password: String!){\n    loginUser(email:$email, password: $password) {\n        token,\n    }\n  }\n"): (typeof documents)["\n  mutation LoginUsr($email: String!, $password: String!){\n    loginUser(email:$email, password: $password) {\n        token,\n    }\n  }\n"];
/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function gql(source: "\n  mutation CreateUsr( $email: String!, $name: String!, $password: String!){\n    createUser(email:$email, name:$name, password: $password) {\n        user {\n          identifier,\n          name,\n          email,\n        }\n    }\n  }\n"): (typeof documents)["\n  mutation CreateUsr( $email: String!, $name: String!, $password: String!){\n    createUser(email:$email, name:$name, password: $password) {\n        user {\n          identifier,\n          name,\n          email,\n        }\n    }\n  }\n"];
/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function gql(source: "\n  query Parking {\n    allParkings {\n        identifier\n        name\n        address\n        totalLots\n        occupiedLots\n        entries {\n            entryType\n            createdAt\n        }\n    }\n}\n"): (typeof documents)["\n  query Parking {\n    allParkings {\n        identifier\n        name\n        address\n        totalLots\n        occupiedLots\n        entries {\n            entryType\n            createdAt\n        }\n    }\n}\n"];
/**
 * The gql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function gql(source: "\n  query GetParking($identifier: String!) {\n    parking(identifier: $identifier) {\n        identifier\n        name\n        address\n        totalLots\n        occupiedLots\n        entries {\n          entryType\n          createdAt\n        }\n    }\n}\n"): (typeof documents)["\n  query GetParking($identifier: String!) {\n    parking(identifier: $identifier) {\n        identifier\n        name\n        address\n        totalLots\n        occupiedLots\n        entries {\n          entryType\n          createdAt\n        }\n    }\n}\n"];

export function gql(source: string) {
  return (documents as any)[source] ?? {};
}

export type DocumentType<TDocumentNode extends DocumentNode<any, any>> = TDocumentNode extends DocumentNode<  infer TType,  any>  ? TType  : never;
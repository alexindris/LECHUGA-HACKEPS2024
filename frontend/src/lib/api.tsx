import { gql } from "@/__generated__";

export const GET_HEALTH = gql(/* GraphQL */ `
  query Health {
    health {
      status
      time
    }
  }
`);
export const LOGIN_USER = gql(`
  mutation LoginUsr($email: String!, $password: String!){
    loginUser(email:$email, password: $password) {
        token,
    }
  }
`);

export const CREATE_USER = gql(`
  mutation CreateUsr( $email: String!, $name: String!, $password: String!){
    createUser(email:$email, name:$name, password: $password) {
        user {
          identifier,
          name,
          email,
        }
    }
  }
`);

export const GET_ALL_PARKINGS = gql(`
  query Parking {
    allParkings {
        identifier
        name
        address
        totalLots
        occupiedLots
        entries {
            entryType
            createdAt
        }
    }
}
`);

export const GET_PARKING = gql(`
  query GetParking($identifier: String!) {
    parking(identifier: $identifier) {
        identifier
        name
        address
        totalLots
        occupiedLots
        entries {
          entryType
          createdAt
        }
    }
}
`);

export const CREATE_PARKING = gql(`
  mutation CreateParkingg($name: String!, $address: String!, $totalLots: Int!){
    createParking( address: $address, name: $name, totalLots: $totalLots) {
      parking {
        identifier
        name
        address
        totalLots
        occupiedLots
        entries {
            entryType
            createdAt
        }
      }
    }
}
`);

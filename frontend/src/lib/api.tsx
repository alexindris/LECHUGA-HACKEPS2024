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

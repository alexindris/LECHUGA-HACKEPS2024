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
  mutation LoginUser($email: String!, $password: String!){
    loginUser(email:$email, password: $password) {
        token,
    }
  }
`);

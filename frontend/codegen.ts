import type { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  // schema: "http://localhost:8000/graphql/",
  schema: "../backend/schema.graphql",
  documents: ["src/**/*.tsx"],
  ignoreNoDocuments: true,
  generates: {
    "./src/__generated__/": {
      preset: "client",
      plugins: [],
      presetConfig: {
        gqlTagName: "gql",
      },
    },
  },
  // "./schema.graphql": {
  //   plugins: ["schema-ast"],
  //   config: {
  //     includeDirectives: true,
  //   },
  // },
};

export default config;

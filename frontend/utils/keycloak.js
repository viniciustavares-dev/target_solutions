import Keycloak from "keycloak-js";

const keycloak = new Keycloak({
  realm: process.env.NEXT_PUBLIC_KEYCLOAK_REALM,
  authServerUrl: process.env.NEXT_PUBLIC_KEYCLOAK_AUTH_URL,
  clientId: process.env.NEXT_PUBLIC_KEYCLOAK_CLIENT_ID,
});

export default keycloak;
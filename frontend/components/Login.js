import keycloak from "../utils/keycloak";
import { Button } from "@chakra-ui/react";

export default function Login() {
  const handleLogin = () => {
    keycloak.init({ onLoad: "login-required" });
  };

  return (
    <Button onClick={handleLogin}>Login com Keycloak</Button>
  );
}
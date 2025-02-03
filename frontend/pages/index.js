// pages/index.js
import PrivateRoute from "../components/PrivateRoute";
import { Container, Heading } from "@chakra-ui/react";

export default function Dashboard() {
  return (
    <PrivateRoute roles={["usuario"]}>
      <Container>
        <Heading>Dashboard</Heading>
        {/* Conteúdo do dashboard */}
      </Container>
    </PrivateRoute>
  );
}
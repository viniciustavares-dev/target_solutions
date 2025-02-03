import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import keycloak from "../utils/keycloak";

export default function PrivateRoute({ children, roles }) {
  const router = useRouter();
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [hasRequiredRole, setHasRequiredRole] = useState(false);

  useEffect(() => {
    keycloak.init({ onLoad: "check-sso" }).then((authenticated) => {
      setIsAuthenticated(authenticated);
      if (authenticated) {
        const userRoles = keycloak.tokenParsed.realm_access.roles;
        const requiredRole = roles.some((role) => userRoles.includes(role));
        setHasRequiredRole(requiredRole);
        if (!requiredRole) {
          router.push("/unauthorized"); // Redireciona para página de não autorizado
        }
      } else {
        router.push("/login"); // Redireciona para página de login
      }
    });
  }, []);

  if (!isAuthenticated) {
    return <div>Carregando...</div>;
  }

  if (!hasRequiredRole) {
    return <div>Não autorizado.</div>;
  }

  return children;
}
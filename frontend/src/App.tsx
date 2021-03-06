import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Unauthorized from "./pages/Unauthorized";
import Home from "./pages/Home";
import Logout from "./pages/Logout";

export default function App(): JSX.Element {
  return (
    <Router>
      <Switch>
        <Route path="/desautorizado">
          <Unauthorized />
        </Route>
        <Route path="/logout">
          <Logout />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}

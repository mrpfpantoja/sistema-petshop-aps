import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx"; // O App.jsx já vai puxar o App.css completo

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
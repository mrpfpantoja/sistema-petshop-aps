import React, { useState } from 'react';
import './App.css';
import Sidebar from './components/Sidebar';
import Inicio from './pages/Inicio';
import Consultas from './pages/Consultas';
import Produtos from './pages/Produtos';
import Perfil from './pages/Perfil';
import Configuracoes from './pages/Configuracoes';

function App() {
  // Estado que armazena qual tela está visível no momento
  const [abaAtiva, setAbaAtiva] = useState('inicio');

  // Função auxiliar para renderizar a página correta baseado no estado
  const renderPagina = () => {
    switch (abaAtiva) {
      case 'inicio':
        return <Inicio />;
      case 'consultas':
        return <Consultas />;
      case 'produtos':
        return <Produtos />;
      case 'perfil':
        return <Perfil />;
      case 'configuracoes':
        return <Configuracoes />;
      default:
        return <Inicio />;
    }
  };

  return (
    <div style={{ display: 'flex', width: '100vw', minHeight: '100vh' }}>
      {/* Menu Lateral Fixo */}
      <Sidebar abaAtiva={abaAtiva} setAbaAtiva={setAbaAtiva} />
      
      {/* Conteúdo Dinâmico */}
      <main className="content">
        {renderPagina()}
      </main>
    </div>
  );
}

export default App;
import React from 'react';

export default function Configuracoes() {
  return (
    <>
      <h1>⚙️ Configurações</h1>
      <div className="box" style={{ maxWidth: '500px' }}>
        <h3>Preferências do Sistema</h3>
        <div className="item" style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', padding: '15px' }}>
          <div>
            <strong>Notificações por WhatsApp</strong> <br />
            <small>Avisar clientes automaticamente sobre consultas</small>
          </div>
          <input type="checkbox" defaultChecked style={{ transform: 'scale(1.3)', cursor: 'pointer' }} />
        </div>
        <div className="item" style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', padding: '15px' }}>
          <div>
            <strong>Modo Escuro (Dark Mode)</strong> <br />
            <small>Alterar a interface para cores escuras</small>
          </div>
          <input type="checkbox" style={{ transform: 'scale(1.3)', cursor: 'pointer' }} />
        </div>
      </div>
    </>
  );
}
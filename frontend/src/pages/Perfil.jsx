import React from 'react';

export default function Perfil() {
  const handleSave = (e) => {
    e.preventDefault();
    alert('Dados do perfil salvos com sucesso!');
  };

  return (
    <>
      <h1>👤 Meu Perfil</h1>
      <div className="box" style={{ maxWidth: '600px' }}>
        <h3>Dados do Usuário</h3>
        {/* CORRIGIDO: flex-direction mudou para flexDirection */}
        <form onSubmit={handleSave} style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '15px' }}>
          <div>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Nome Completo:</label>
            <input type="text" defaultValue="Lucas Costa" style={{ width: '100%', padding: '8px', borderRadius: '5px', border: '1px solid #ccc' }} />
          </div>
          
          <div>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>E-mail:</label>
            <input type="email" defaultValue="lucas@email.com" style={{ width: '100%', padding: '8px', borderRadius: '5px', border: '1px solid #ccc' }} />
          </div>

          {/* Adicionado campo de telefone conforme a documentação inicial do sistema */}
          <div>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Telefone:</label>
            <input type="text" defaultValue="(83) 99999-9999" style={{ width: '100%', padding: '8px', borderRadius: '5px', border: '1px solid #ccc' }} />
          </div>

          <button type="submit" style={{ background: '#1abc9c', color: 'white', border: 'none', padding: '10px', borderRadius: '5px', fontWeight: 'bold', cursor: 'pointer' }}>
            Salvar Alterações
          </button>
        </form>
      </div>
    </>
  );
}
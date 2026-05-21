import React from 'react';

export default function Inicio() {
  return (
    <>
      <h1>Bem-vindo ao PetShop System!</h1>
      <div className="cards">
        <div className="card" onClick={() => alert('Agendar Consulta clicado!')}>📅 Agendar Consulta</div>
        <div className="card">🚨 Emergência</div>
        <div className="card">💉 Vacinas Pendentes</div>
        <div className="card">📋 Histórico</div>
      </div>

      <div className="grid">
        {/* AGENDAMENTOS */}
        <div className="box">
          <h3>Próximos Agendamentos</h3>
          <div className="item">
            🐶 Rex - Consulta Veterinária <br />
            <small>15/05/2026 - 14:00</small>
          </div>
          <div className="item">
            🐱 Mia - Banho e Tosa <br />
            <small>18/05/2026 - 10:00</small>
          </div>
        </div>

        {/* MEUS PETS */}
        <div className="box">
          <h3>Meus Pets</h3>
          <div className="item">🐶 Rex - Labrador</div>
          <div className="item">🐱 Mia - Persa</div>
        </div>
      </div>
    </>
  );
}
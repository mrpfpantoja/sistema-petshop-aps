import React from 'react';

export default function Consultas() {
  return (
    <>
      <h1>🩺 Histórico de Consultas</h1>
      <div className="box">
        <h3>Filtrar por Pet</h3>
        <div style={{ display: 'flex', gap: '10px' }}>
          <button style={{ padding: '8px 15px', cursor: 'pointer' }}>Todos</button>
          <button style={{ padding: '8px 15px', cursor: 'pointer' }}>Rex</button>
          <button style={{ padding: '8px 15px', cursor: 'pointer' }}>Mia</button>
        </div>
      </div>

      <div className="box">
        <h3>Prontuários Recentes</h3>
        <div className="item">
          <strong>🐶 Rex (Labrador)</strong>
          <p>Motivo: Vacinação Anual (V10 + Antirrábica). Animal saudável.</p>
          <small>Veterinário: Dr. Carlos - 10/04/2026</small>
        </div>
        <div className="item">
          <strong>🐱 Mia (Persa)</strong>
          <p>Motivo: Limpeza de tártaro e check-up geral.</p>
          <small>Veterinária: Dra. Ana - 22/03/2026</small>
        </div>
      </div>
    </>
  );
}
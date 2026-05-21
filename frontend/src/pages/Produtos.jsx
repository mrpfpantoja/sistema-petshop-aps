import React from 'react';

export default function Produtos() {
  return (
    <>
      <h1>🛍️ Estoque de Produtos</h1>
      <div className="cards" style={{ marginBottom: '20px' }}>
        <div className="card" style={{ background: '#27ae60' }}>📦 Total Itens: 142</div>
        <div className="card" style={{ background: '#e67e22' }}>⚠️ Estoque Baixo: 5</div>
        <div className="card" style={{ background: '#2980b9' }}>🛒 Fornecedores: 12</div>
      </div>

      <div className="grid">
        <div className="box">
          <h3>Rações e Alimentos</h3>
          <div className="item">
            <span><strong>Ração Premium Cães Adultos 15kg</strong></span>
            <small>Qtd: 24 unidades | Preço: R$ 189,90</small>
          </div>
        </div>
        <div className="box">
          <h3>Higiene e Acessórios</h3>
          <div className="item">
            <span><strong>Shampoo Neutro para Pets 500ml</strong></span>
            <small>Qtd: 3 unidades <span style={{ color: 'red' }}>(Repor!)</span> | Preço: R$ 32,00</small>
          </div>
        </div>
      </div>
    </>
  );
}
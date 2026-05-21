import React from 'react';

export default function Sidebar({ abaAtiva, setAbaAtiva }) {
  const menus = [
    { id: 'inicio', label: '🏠 Início' },
    { id: 'consultas', label: '🩺 Consultas' },
    { id: 'produtos', label: '🛍️ Produtos' },
    { id: 'perfil', label: '👤 Perfil' },
    { id: 'configuracoes', label: '⚙️ Configurações' },
  ];

  return (
    <aside className="sidebar">
      <h2>PetShop</h2>
      <input type="text" placeholder="Pesquisar..." />
      <nav>
        <ul>
          {menus.map((menu) => (
            <li 
              key={menu.id} 
              className={abaAtiva === menu.id ? 'active' : ''}
              onClick={() => setAbaAtiva(menu.id)}
            >
              <button className="menu-item">{menu.label}</button>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
}
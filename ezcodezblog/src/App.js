import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavBar from './Components/Navbar/NavBar';
import { Blog } from './Components/Blog/Blog';
import CodeSection from './Components/CodeSection/CodeSection';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <NavBar />
        <Routes>
            <Route element={<Blog />} path='' />
            <Route element={<CodeSection />} path='codes' />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
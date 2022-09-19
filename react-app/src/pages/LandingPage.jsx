
import { Modelo1} from "./Modelos/Modelo1"
import { Modelo2} from "./Modelos/Modelo2"

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { Home } from "./Home";
import  styles from "./MLApp.module.css"
import { createContext } from "react";
export function LandingPage(){
    const TabsContext = createContext(null);
        return(
            
            <Router>
        

            <div >

            
            <Routes>
            <Route path='/' element={<Home/>}></Route>
            <Route path='/Inicio' element={<Home/>}></Route>
            <Route path='/Modelo I' element={<Modelo1/>}></Route>
            <Route path='/Modelo II' element={<Modelo2/>}></Route>

            </Routes>
                
            </div>
            </Router>
        
                
        )
}
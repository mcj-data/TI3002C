import { cloneElement, useState } from "react";
import styles from "./Menu.module.css";
import { useLocation } from 'react-router-dom'

export function Menu(props) {
    const location = useLocation();
    let [activeTab, setActiveTab] = useState(location.pathname.replace("/",""))
  
    const handleTabs = (key,event) => {
        
        
    };
    return (
        <div className={styles.Menu}>
        {props.children.map((child,i)=>cloneElement(child, {onTabClick : handleTabs,activeTab:activeTab, setActiveTab:setActiveTab ,tab:i, key:i}))}
            
        </div>
    );
    }

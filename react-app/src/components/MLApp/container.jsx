import styles from "../../pages/MLApp.module.css"
import { Menu } from "../Menu"
import { Sidebar } from "../Sidebar"
import { Footer } from "../Footer"

import { Tab } from "../Tab"


export function Container(props){
    
    return(
        <div className={styles.Main}>
        <Sidebar />
        <Menu>
            <Tab>Inicio</Tab>
            <Tab>Modelo I</Tab>
            <Tab>Modelo II</Tab>
            <Tab>Menu II</Tab>

            </Menu>
        <div className={styles.App}>
            <div className={styles.Title}>
                {props.title}
            </div>
            {props.children}
        </div>
        <Footer />

        </div>
    )
}
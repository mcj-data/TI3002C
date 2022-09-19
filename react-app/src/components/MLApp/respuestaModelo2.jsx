import styles from "../../pages/Modelos/Modelos.module.css"

export function RespuestaModelo2(props){
    let response = props.response[0]
    
    return(
        
            <div className={styles.ResponseCard}>
            <div className={styles.ResponseCardTitle}>
                Title
            </div>
            <div className={styles.ResponseCardBody}>
                {response.Prediction}
            </div>
            <div className={styles.ResponseCardBody}>
            {response.Accuracy}
            </div>
            </div>
        
    )
}
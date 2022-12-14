import { useRecordContext } from 'react-admin';
const DetailFields = (source)=>{
    const record = useRecordContext();
    return (
        <details >
            <summary>Click Here</summary>
            <p>{record && record[source.source]}</p>
        </details>
    )
}

export default DetailFields
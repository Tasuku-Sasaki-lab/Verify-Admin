import * as React from 'react'
import { DateField } from 'react-admin'

const CustomDateField = ({ ...props }) => {
  return <DateField showTime={true} locales="ja" {...props} />
}
export default CustomDateField

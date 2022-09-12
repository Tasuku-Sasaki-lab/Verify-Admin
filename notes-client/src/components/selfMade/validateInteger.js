const validateInteger = (value) => {
    if (!Number.isInteger(value)) {
        return 'Must be Integer';
    }
    return undefined;
}

export default validateInteger;
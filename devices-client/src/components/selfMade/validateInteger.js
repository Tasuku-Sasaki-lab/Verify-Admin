const validateInteger = (value) => {
    if (!Number.isInteger(value)) {
        return '整数を入力してください。';
    }
    return undefined;
}

export default validateInteger;
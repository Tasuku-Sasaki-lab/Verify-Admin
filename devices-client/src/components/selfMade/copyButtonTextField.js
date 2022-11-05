import React, { useState } from 'react';
import FormControl     from '@material-ui/core/FormControl';
import OutlinedInput   from '@material-ui/core/OutlinedInput';
import IconButton      from '@material-ui/core/IconButton';
import InputAdornment  from '@material-ui/core/InputAdornment';
import AssignmentIcon  from '@material-ui/icons/Assignment';
import Tooltip         from '@material-ui/core/Tooltip';
import CopyToClipBoard from 'react-copy-to-clipboard';


const CopyButtomTextField: React.FC = () => {
  const [input,   setInput]   = useState<string>('');
  const [openTip, setOpenTip] = useState<boolean>(false);

  const handleChangeText = (e: React.ChangeEvent<HTMLInputElement>): void => {
    setInput(e.target.value);
  };

  const handleCloseTip = (): void => {
    setOpenTip(false);
  };

  const handleClickButton = (): void => {
    setOpenTip(true);
  };

  return (
    <FormControl
      variant='outlined'
    >
      <OutlinedInput
        type='text'
        value={input}
        onChange={handleChangeText}
        endAdornment={
          <InputAdornment position="end">
            <Tooltip
              arrow
              open={openTip}
              onClose={handleCloseTip}
              disableHoverListener
              placement='top'
              title='Copied!'
            >
              <CopyToClipBoard text={input}>
                <IconButton
                  disabled={input === ''}
                  onClick={handleClickButton}
                >
                  <AssignmentIcon />
                </IconButton>
              </CopyToClipBoard>
            </Tooltip>
          </InputAdornment>
        }
      />
    </FormControl>
  );
};

export default CopyButtomTextField;
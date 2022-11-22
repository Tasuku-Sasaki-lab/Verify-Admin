import { useCallback, useState } from 'react';
import { useRecordContext } from 'react-admin';
import {CopyToClipboard} from 'react-copy-to-clipboard';
import { makeStyles } from '@material-ui/core';
import classNames from 'classnames';
import { Button } from '@material-ui/core';
import SvgIcon from '@material-ui/core/SvgIcon';
import DoneOutlineIcon from '@material-ui/icons/DoneOutline';
import FileCopyOutlinedIcon from '@material-ui/icons/FileCopyOutlined';


const useStyles = makeStyles(() =>({
  field: {
    position: 'relative',
    cursor: 'pointer',
    },
  row : {
    position: 'relative',
    display: 'block',
    zIndex: 5,
    width: '100%',
    '&:hover': {
      '& $icon': {
        display: 'block',
      },
    },
    '& button': {
      width: `100%`,
      display: 'block',
      textTransform: 'none',
      'font-weight': 400,
      'text-align': 'left',
      'font-size': '0.875rem',
      'line-height': 1.43,
      'letter-spacing': '0.01071em',
    },
  },

  icon: {
    display: 'none',
    height: '40%',
    position: 'absolute',
    top: '0.2em',
    left: '-1.5em',
    zIndex: 10,
    padding: '0.2em',
  },
  
}));

const CopyTextField = (source) => {
  const record = useRecordContext();
  const classes = useStyles();
  const [wasCopied, setWasCopied] = useState(false);
  const handleMouseLeave = useCallback(() => setWasCopied(false), []);
  const handleCopied = useCallback(() => setWasCopied(true), []);
  console.log(record);
  if (!record) {
    return null;
  }
  const text = record.command;
  if(!text){
    return null;
  }
  return (
    <div className={classes.field}>
      <div className={classes.row} onMouseLeave={handleMouseLeave}>
          <SvgIcon
                className={classNames(classes.icon)}
                component={wasCopied ? DoneOutlineIcon : FileCopyOutlinedIcon}
              />
            <CopyToClipboard text={text} onCopy={handleCopied}>
            <Button>
              {text}
            </Button>
          </CopyToClipboard>
        </div>
      </div>
  );
}

export default CopyTextField;

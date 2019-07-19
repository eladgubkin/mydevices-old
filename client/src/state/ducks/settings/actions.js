/* ACTION CREATOR FUNCTIONS
Put here the functions that return an action object that can be dispatched
HINT: Always use functions for consistency, don't export plain objects
*/

import * as types from './types';

const changeTab = tab => ({
  type: types.CHANGE_TAB,
  payload: {
    tab
  }
});

export { changeTab };
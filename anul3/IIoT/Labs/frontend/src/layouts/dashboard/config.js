import BellIcon from '@heroicons/react/24/solid/BellIcon'
import { SvgIcon } from '@mui/material';

export const items = [
  {
    title: 'Activity',
    items: [
      {
        title: 'Notifications',
        path: '/notifications',
        icon: (
          <SvgIcon fontSize="small">
            <BellIcon />
          </SvgIcon>
        )
      }
    ]
  },
]

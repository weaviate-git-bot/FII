import PropTypes from 'prop-types';
import { Avatar, Card, CardContent, Stack, SvgIcon, Typography } from '@mui/material';
import DeviceThermostatIcon from '@mui/icons-material/DeviceThermostat';
import OpacityIcon from '@mui/icons-material/Opacity';
import ThreeDRotationIcon from '@mui/icons-material/ThreeDRotation';
import { format } from "date-fns";

const sensorTypes = {
    1: 'Soil Moisture',
    2: 'Temperature',
    3: 'Tilt',
}

const iconTypes = {
    1: <OpacityIcon />,
    2: <DeviceThermostatIcon />,
    3: <ThreeDRotationIcon />,
}

export const OverviewBudget = (props) => {
  const { sensorType, timestamp, location, sx, value } = props;

  return (
    <Card sx={sx}>
      <CardContent>
        <Stack
          alignItems="flex-start"
          direction="row"
          justifyContent="space-between"
          spacing={3}
        >
          <Stack spacing={1}>
            <Typography
              color="text.secondary"
              variant="overline"
            >
              {sensorTypes[sensorType]}
            </Typography>
            <Typography variant="h4">
              {value}
            </Typography>
          </Stack>
          <Avatar
            sx={{
              backgroundColor: 'success.main',
              height: 56,
              width: 56
            }}
          >
            <SvgIcon>
              { iconTypes[sensorType] }
            </SvgIcon>
          </Avatar>
        </Stack>
        <Stack
        alignItems="center"
        direction="row"
        spacing={2}
        sx={{ mt: 2 }}
        >
        <Typography
            color="text.secondary"
            variant="caption"
        >
            At {format(new Date(timestamp),"dd/MM/yyyy HH:mm:ss")} ({ location })
        </Typography>
        </Stack>
      </CardContent>
    </Card>
  );
};

OverviewBudget.prototypes = {
  sensorType: PropTypes.number,
  difference: PropTypes.number,
  location: PropTypes.string,
  positive: PropTypes.bool,
  sx: PropTypes.object,
  timestamp: PropTypes.string,
  value: PropTypes.string.isRequired
};
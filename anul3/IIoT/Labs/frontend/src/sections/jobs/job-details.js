import {
  TextField,
  Typography,
  CardContent,
  Grid,
  Container,
  Divider,
  List,
  ListItem,
  ListItemText,
} from "@mui/material";
import PropTypes from "prop-types";
import { Box } from "@mui/system";
import CurrencyDollarIcon from "@heroicons/react/24/solid/CurrencyDollarIcon";
import { OverviewBudget } from "./card";

export const JobDetails = (props) => {
  const textStyle = {
    flex: "1 1 auto",
    minWidth: "0px",
    display: "flex",
    flexDirection: "row",
    marginTop: "0px",
    marginBottom: "0px",
  };
  const boxStyle = {
    flex: "1 1 0%",
    marginTop: "0px",
  };
  const listItemRoot = {
    display: "flex",
    "-webkit-box-pack": "start",
    justifyContent: "flex-start",
    "-webkit-box-align": "center",
    alignItems: "center",
    position: "relative",
    textDecoration: "none",
    width: "100%",
    boxSizing: "border-box",
    textAlign: "left",
    padding: "12px 24px",
  };
  const { notification } = props;
  const data = [
    {
      key: "Name",
      value: notification?.name,
    },
    {
      key: "Description",
      value: notification?.description,
    },
    {
      key: "Involved sensors",
      value: 'Here is a list of all the sensors involved in this notification',
    },
  ];
  return (
    <CardContent>
      <Grid
        item
        xs={12}
        md={6}
        sx={{
          paddingLeft: "24px",
        }}
      >
        <Typography variant="h6">Notification Details</Typography>
        <Divider
          sx={{
            margin: "16px",
          }}
        />
        <List
          sx={{
            listStyle: "none",
            margin: "0px",
            padding: "0px",
            position: "relative",
          }}
        >
          {data.map((item, index) => (
            <ListItem sx={listItemRoot} key={`description-${item.name}`}>
              <ListItemText sx={textStyle}>
                <Typography variant="title" component="h6">
                  {item.key}
                </Typography>
                <Box sx={boxStyle}>
                  <Typography variant="body2" component="h6">
                    {item.value}
                  </Typography>
                </Box>
              </ListItemText>
            </ListItem>
          ))}
          <ListItem sx={listItemRoot}>
            <Container maxWidth="xl">
              <Grid container spacing={3}>
                {notification?.sensorReadings?.map((sensorReading, index) => (
                  <Grid xs={12} sm={6} lg={3}>
                    <OverviewBudget
                      key={`sensor-${index}`}
                      sensorType={sensorReading?.type}
                      value={sensorReading?.value}
                      icon={<CurrencyDollarIcon />}
                      location={sensorReading?.location}
					  timestamp={sensorReading?.timestamp}
                    />
                  </Grid>
                ))}
              </Grid>
            </Container>
          </ListItem>
        </List>
        <Divider
          sx={{
            margin: "16px",
          }}
        />
      </Grid>
    </CardContent>
  );
};

JobDetails.propTypes = {
  job: PropTypes.object,
};

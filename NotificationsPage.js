import { Box, Container, List, ListItem, ListItemText, Typography } from "@mui/material";

const NotificationsPage = () => (
  <Container sx={{ p: 3 }}>
    <Typography variant="h4" gutterBottom>
      Notifications
    </Typography>
    <Typography color="text.secondary" paragraph>
      Receive reminders for deadlines, interview preparation, and follow-up communications.
    </Typography>
    <List>
      <ListItem>
        <ListItemText primary="No notifications yet" secondary="Your reminders will appear here when scheduled." />
      </ListItem>
    </List>
  </Container>
);

export default NotificationsPage;

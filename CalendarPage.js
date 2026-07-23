import { Box, Container, Typography } from "@mui/material";

const CalendarPage = () => (
  <Container sx={{ p: 3 }}>
    <Typography variant="h4" gutterBottom>
      Interview Calendar
    </Typography>
    <Typography color="text.secondary">
      Visualize upcoming interviews, assessment deadlines, and follow-up actions with a calendar-focused timeline.
    </Typography>
  </Container>
);

export default CalendarPage;

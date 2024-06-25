import { createBrowserRouter } from 'react-router-dom';

import App from 'app';
import {
  EditCarPage,
  CarsPage,
  ProfilePage,
  RegistrationPage,
  SchedulePage,
  HomePage,
} from 'pages';
import { rootStore } from 'app/store';
import { Flex, Typography } from 'antd';

export const router = createBrowserRouter([
  {
    id: 'root',
    path: '/',
    loader: async () => rootStore.auth.refreshTokens(),
    element: <App />,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: 'registration',
        element: <RegistrationPage />,
      },
      {
        path: 'profile',
        element: <ProfilePage />,
      },
      {
        path: 'cars',
        element: <CarsPage />,
      },
      {
        path: 'cars/:carId',
        element: <EditCarPage />,
      },
      {
        path: 'schedule',
        element: <SchedulePage />,
      },
      {
        path: 'manage/schedule',
        element: <SchedulePage />,
      },

      {
        path: '*',
        element: (
          <Flex align="center" justify="center" style={{ marginTop: '100px' }}>
            <Typography.Title level={3} type="danger">
              Page not found
            </Typography.Title>
          </Flex>
        ),
      },
    ],
  },
]);

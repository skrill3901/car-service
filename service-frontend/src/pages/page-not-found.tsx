import { Flex, Typography } from 'antd';

const PageNotFound = () => {
  return (
    <Flex align="center" justify="center" style={{ marginTop: '100px' }}>
      <Typography.Title level={3} type="danger">
        Page not found
      </Typography.Title>
    </Flex>
  );
};

export default PageNotFound;

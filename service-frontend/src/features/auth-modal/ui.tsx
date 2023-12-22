import { FC, useState } from 'react';
import { observer } from 'mobx-react-lite';
import { Link, useNavigate } from 'react-router-dom';

import { useStore } from 'app/store';

import { Button, Checkbox, Form, Input, Modal } from 'antd';
import { LockOutlined, UserOutlined } from '@ant-design/icons';

type FieldType = {
  username: string;
  password: string;
  remember: boolean;
};

const AuthModal: FC = () => {
  const navigate = useNavigate();
  const [form] = Form.useForm<FieldType>();

  const { auth, profile } = useStore();

  const [open, setOpen] = useState(false);

  const close = () => {
    setOpen(false);
  };

  const onFinish = (values: FieldType) => {
    auth.logIn(values).then((status) => {
      if (status === 'idle') {
        setOpen(false);
        profile.getProfile();
        navigate('/');
      }
    });
  };

  return (
    <>
      <Button type="primary" onClick={() => setOpen(true)}>
        Log In
      </Button>
      <Modal
        title="Auth"
        open={open}
        onOk={() => setOpen(false)}
        onCancel={() => setOpen(false)}
        style={{ maxWidth: '400px' }}
        footer={[
          <Button onClick={close} key="close">
            Close
          </Button>,
        ]}
      >
        <Form name="auth_form" form={form} initialValues={{ remember: true }} onFinish={onFinish}>
          <Form.Item
            name="username"
            rules={[{ required: true, message: 'Please input your Username!' }]}
          >
            <Input
              prefix={<UserOutlined className="site-form-item-icon" />}
              placeholder="Username"
            />
          </Form.Item>
          <Form.Item
            name="password"
            rules={[{ required: true, message: 'Please input your Password!' }]}
          >
            <Input.Password
              prefix={<LockOutlined className="site-form-item-icon" />}
              type="password"
              placeholder="Password"
            />
          </Form.Item>
          <Form.Item>
            <Form.Item name="remember" valuePropName="checked" noStyle>
              <Checkbox>Remember me</Checkbox>
            </Form.Item>
            <Link to="/" style={{ float: 'right' }} onClick={close}>
              Forgot password
            </Link>
          </Form.Item>
          <Form.Item>
            <Button
              type="primary"
              htmlType="submit"
              style={{ width: '100%' }}
              loading={auth.loadingStatus === 'loading'}
            >
              Log in
            </Button>
          </Form.Item>
          Or{' '}
          <Link to="/registration" onClick={close}>
            register now!
          </Link>
        </Form>
      </Modal>
    </>
  );
};

export default observer(AuthModal);
